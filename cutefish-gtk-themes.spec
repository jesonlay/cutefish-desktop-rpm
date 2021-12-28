%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name gtk-themes

Name: cutefish-%{component_name}
Version: 0.7
Release: 1%{?dist}
License: GPLv3
Summary: System default icon theme for Cutefish Desktop

BuildRequires:  cmake make gcc gcc-c++

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz

%description
new gtk theme for gtk app

%prep
%setup -qn %{component_name}-%{version}

%build
cmake -D CMAKE_INSTALL_PREFIX=/usr .
%make_build

%install
%make_install

%files
%license LICENSE
%{_datadir}/themes/Cutefish
%{_datadir}/themes/Cutefish-light
%{_datadir}/themes/Cutefish-dark
