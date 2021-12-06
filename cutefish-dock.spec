%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name dock

Name: cutefish-%{component_name}
Version: 0.5
Release: 1%{?dist}
License: GPLv3
Summary: Desktop Taskbar for Cutefish Desktop

BuildRequires: cmake
BuildRequires: qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtx11extras-devel qt5-linguist
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: fishui-devel

Requires: libcutefish
Requires: fishui

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%description
Cutefish Desktop application dock

%prep
%setup -qn %{component_name}-%{version}

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
%{_bindir}/cutefish-dock
%{_datadir}/cutefish-dock
