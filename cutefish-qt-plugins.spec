%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name qt-plugins
%define _qt5pluginsdir %{_libdir}/qt5/plugins

Name: cutefish-%{component_name}
Version: 0.3
Release: 0b%{?dist}
License: GPLv3
Summary: Qt platform theme plugin, unified style, for Cutefish Desktop

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: libqtxdg-devel libxcb-devel xcb-util-wm-devel
BuildRequires: cmake(Qt5Core) cmake(Qt5Widgets) cmake(Qt5DBus) cmake(Qt5QuickControls2) cmake(Qt5X11Extras) cmake(Qt5Gui) cmake(dbusmenu-qt5) cmake(Qt5ThemeSupport)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: qt5-qtbase-static qt5-qtbase-private-devel

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%description
Unify Qt application style of Cutefish Desktop

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
%{_qt5pluginsdir}/platformthemes/libcutefishplatformtheme.so
%{_qt5pluginsdir}/styles/libcutefishstyle.so
