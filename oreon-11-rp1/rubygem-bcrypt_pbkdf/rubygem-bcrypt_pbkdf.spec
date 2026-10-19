%global source0_hash c2414c23ce66869b3eb9f643d6a3374d8322dfb5078125c82792304c10b94cf6
%global gem_name bcrypt_pbkdf
Name: rubygem-%{gem_name}
Version: 1.1.2
Release:        1%{?dist}
Summary:        OpenBSD's bcrypt_pbkdf (a variant of PBKDF2 with bcrypt-based PRF)
License: MIT AND BSD-2-Clause AND BSD-4-Clause AND ISC
URL: https://github.com/net-ssh/bcrypt_pbkdf-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-bcrypt_pbkdf-1.1.2-Fix-compatibility-with-minitest-6.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This gem implements bcrypt_pbkdf (a variant of PBKDF2 with bcrypt-based
PRF).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

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

( cd .%{gem_instdir}
ruby -Itest:${OLDPWD}%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bcrypt_pbkdf-doc -f %{oreon_filedir}/rubygem-bcrypt_pbkdf-doc.list

%changelog

%autochangelog
