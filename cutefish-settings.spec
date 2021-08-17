%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name settings

Name: cutefish-%{component_name}
Version: 0.3
Release: 3%{?dist}
License: GPLv3
Summary: System settings for Cutefish Desktop

BuildRequires: cmake pkgconfig
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtx11extras-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires: kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel
BuildRequires: libicu-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: fishui-devel

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%define _patch0_refspec 15e346d0b964b42dbdd8804cf42489a389138993
Patch0: https://pagure.io/cutefish-desktop-rpm/raw/%{_patch0_refspec}/f/patches/%{name}/0000-use_all_backgrounds.patch
%define _patch1_refspec 2d90cbfdbe38a18c763309cc7a88f043e3dbb842
Patch1: https://pagure.io/cutefish-desktop-rpm/raw/%{_patch1_refspec}/f/patches/%{name}/0001-use_fedora_logo.patch

%description
The System Settings application for Cutefish Desktop

%prep
%setup -qn %{component_name}-%{version}

patch src/background.cpp -i %{PATCH0}
patch src/qml/About/Main.qml -i %{PATCH1}

%build
%{set_build_flags}
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
