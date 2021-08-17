Name: cutefish-extras
Version: 0.20210805.2
Release: 0a%{?dist}
License: MIT
Summary: cutefish-extras repository

Requires: rpmfusion-free-release

Source0: https://gitlab.com/-/snippets/2157880/raw/main/cutefish-extras.repo

%description
This package installs the cutefish-extras repository

%prep

%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/yum.repos.d
cp -avx %{SOURCE0} %{buildroot}/%{_sysconfdir}/yum.repos.d/cutefish-extras.repo

%post

%files
%{_sysconfdir}/yum.repos.d/cutefish-extras.repo
