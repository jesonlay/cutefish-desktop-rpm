%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define _libdir32 %{_exec_prefix}/lib

Name: fishui
Version: 0.3
Release: 0a%{?dist}
License: GPLv3
Summary: CutefishOS GUI library, based on Qt Quick

BuildRequires: cmake make
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtx11extras-devel qt5-qtbase-private-devel qt5-qtquickcontrols2-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libxcb-devel xcb-util-wm-devel

Source0: https://github.com/cutefishos/%{name}/archive/refs/tags/%{version}.tar.gz

%description
FishUI is a GUI library based on QQC2 (Qt Quick Controls 2), every Cutefish application uses it

%package devel
Summary: Development headers for FishUI
Requires: %{name} = %{version}-%{release}, cmake
%description devel
This package provides files sufficient to build software against %{name}

%prep
%setup -qn %{name}-%{version}

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
mkdir -p %{buildroot}/%{_libdir}/cmake/
mv -v %{buildroot}/%{_libdir32}/cmake/FishUI %{buildroot}/%{_libdir}/cmake/FishUI ||:

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/libFishUI.so
%{_libdir}/qt5/qml/FishUI
%{_libdir}/qt5/qml/QtQuick/Controls.2/fish-style

%files devel
%{_libdir}/cmake/FishUI
