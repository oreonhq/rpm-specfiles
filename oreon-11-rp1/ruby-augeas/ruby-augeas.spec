%global source0_hash 002bd237d8dce4b918384cc3043254bf5264efe81f663d1c9ac7b41cbe4df8d2
%global gem_name ruby-augeas
Name:           %{gem_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Ruby bindings for Augeas
License:        LGPL-2.1-or-later
URL:            https://augeas.net
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
# oreon:deps
BuildRequires:  augeas-devel
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rdoc)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby bindings for augeas.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

RUBYLIB=.%{gem_extdir_mri} ruby -I.%{gem_instdir} .%{gem_instdir}/tests/*.rb
%files -f %{oreon_filedir}/main.list
%files -n ruby-augeas-doc -f %{oreon_filedir}/ruby-augeas-doc.list

%changelog

%autochangelog
