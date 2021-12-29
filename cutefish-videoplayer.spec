%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name videoplayer
%define git_refspec 176a8932ce4507e6bc92ef9da29fb2510fc3cd5f
%define git_refspec_short %(echo %{git_refspec} | cut -c -7)

Name: cutefish-%{component_name}
Version: 0.5
#Version: 0.0.0git.%{git_refspec}
Release: 0a.extra
License: GPLv3
Summary: Cutefish Video Player

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel qt5-qtquickcontrols2-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kxmlgui-devel kf5-kdoctools-devel
BuildRequires: plasma-breeze
BuildRequires: mpv-libs-devel

Requires: breeze-icon-theme plasma-breeze-common
Requires: qqc2-desktop-style
Requires: kio-extras
Requires: youtube-dl

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz
#Source0: https://github.com/cutefishos/%{component_name}/tarball/%{git_refspec}#/%{component_name}-%{git_refspec}.tar.gz
Source1: https://github.com/cutefishos/%{component_name}/raw/%{git_refspec}/cutefish-videoplayer.desktop

%description
An open source video player built with Qt/QML and libmpv. Based on haruna

%prep
%setup -qn %{component_name}-%{version}
#%setup -qn cutefishos-%{component_name}-%{git_refspec_short}

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
mkdir -p %{buildroot}/%{_datadir}/applications
cp -ax %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
