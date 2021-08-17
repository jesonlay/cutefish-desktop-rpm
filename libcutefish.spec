%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name: libcutefish
Version: 0.2
Release: 0a%{?dist}
License: GPLv3
Summary: CutefishOS system library

BuildRequires: cmake make
BuildRequires: qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtsensors-devel
BuildRequires: kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel kf5-bluez-qt-devel kf5-kio-devel libkscreen-qt5-devel

Source0: https://github.com/cutefishos/%{name}/archive/refs/tags/%{version}.tar.gz

%description
CutefishOS system library

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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/qt5/qml/Cutefish
