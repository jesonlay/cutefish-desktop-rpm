%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name kwin-plugins
%define _qt5pluginsdir %{_libdir}/qt5/plugins

Name: cutefish-%{component_name}
Version: 0.5
Release: 1%{?dist}
License: GPLv3
Summary: Some configurations and plugins of KWin for Cutefish Desktop

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtx11extras-devel cmake(Qt5UiTools)
BuildRequires: kf5-kconfig-devel kf5-kguiaddons-devel kf5-kcoreaddons-devel kf5-kconfigwidgets-devel kf5-kwindowsystem-devel kf5-kwayland-devel
BuildRequires: kdecoration-devel kwin-devel
BuildRequires: libepoxy-devel

Requires: kwin

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%description
Cutefish Desktop KWin Plugins

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
%{_sysconfdir}/xdg/kglobalshortcutsrc
%{_sysconfdir}/xdg/kwinrc
%{_sysconfdir}/xdg/kwinrulesrc
%{_qt5pluginsdir}/kwin/effects/plugins/libroundedwindow.so
%{_qt5pluginsdir}/org.kde.kdecoration2/libcutefishdecoration.so
%{_datadir}/kwin/effects/cutefish_scale
%{_datadir}/kwin/effects/cutefish_squash
%{_datadir}/kwin/effects/cutefish_popups/
%{_datadir}/kwin/scripts/cutefishlauncher
%{_datadir}/kwin/tabbox/cutefish_thumbnail
