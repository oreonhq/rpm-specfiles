%global source0_hash c2414c23ce66869b3eb9f643d6a3374d8322dfb5078125c82792304c10b94cf6

# Generated from bcrypt_pbkdf-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bcrypt_pbkdf

Name: rubygem-%{gem_name}
Version: 1.1.2
Release: 3%{?dist}
Summary: OpenBSD's bcrypt_pbkdf (a variant of PBKDF2 with bcrypt-based PRF)
# BSD-4-Clause:
#   ext/mri/blf.h
#   ext/mri/blowfish.c
# BSD-2-Clause:
#   ext/mri/hash_sha512.c
# ISC:
#   ext/mri/bcrypt_pbkdf.c
License: MIT AND BSD-2-Clause AND BSD-4-Clause AND ISC
URL: https://github.com/net-ssh/bcrypt_pbkdf-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatiblity with minitest 6
# https://github.com/net-ssh/bcrypt_pbkdf-ruby/pull/28
Patch0: rubygem-bcrypt_pbkdf-1.1.2-Fix-compatibility-with-minitest-6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(minitest) >= 5

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

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
( cd .%{gem_instdir}
ruby -Itest:${OLDPWD}%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/bcrypt_pbkdf.gemspec
%{gem_instdir}/test

%changelog
%autochangelog
