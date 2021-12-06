%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name icons

Name: cutefish-%{component_name}
Version: 0.5
Release: 1%{?dist}
License: GPLv3
Summary: System default icon theme for Cutefish Desktop

BuildRequires:  cmake make gcc gcc-c++
Provides:       crule-icon-theme = 0.0.%{version}-%{release}

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%description
Crule, the system default icon theme for Cutefish Desktop, based on vinceliuice's whitesur

%prep
%setup -qn %{component_name}-%{version}

%build
cmake .
%make_build

%install
%make_install

%files
%license LICENSE
%{_datadir}/icons/Crule
%{_datadir}/icons/Crule-dark
