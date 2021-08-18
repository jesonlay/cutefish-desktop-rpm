%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define git_refspec 4caad74b490543e85dbbc8f49cec067fc493b6f1
%define git_refspec_short %(echo %{git_refspec} | cut -c -7)

Name: libcutefish
#Version: 0.2
Version: 0.2git.%(date +%Y%m%d).%{git_refspec_short}
Release: 1%{?dist}
License: GPLv3
Summary: CutefishOS system library

BuildRequires: cmake make
BuildRequires: qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtsensors-devel
BuildRequires: kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel kf5-bluez-qt-devel kf5-kio-devel libkscreen-qt5-devel

#Source0: https://github.com/cutefishos/%%{name}/archive/refs/tags/%%{version}.tar.gz
Source0: https://github.com/cutefishos/%{name}/tarball/%{git_refspec}#/%{name}-%{git_refspec}.tar.gz

%description
CutefishOS system library

%prep
#%%setup -qn %%{name}-%%{version}
%setup -qn cutefishos-%{name}-%{git_refspec_short}

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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/qt5/qml/Cutefish