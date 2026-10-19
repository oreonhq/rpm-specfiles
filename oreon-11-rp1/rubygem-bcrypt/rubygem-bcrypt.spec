%global source1_hash 48be1badc0e46c86ebf041971ee8f3d416dd597595d04e9852d47d4237ca4ecb
%global source0_hash 8410f8c7b3ed54a3c00cd2456bf13917d695117f033218e2483b2e40b0784099
%global gem_name bcrypt
Name: rubygem-%{gem_name}
Version: 3.1.20
Release:        1%{?dist}
Summary:        Wrapper around bcrypt() password hashing algorithm
License: MIT AND bcrypt-Solar-Designer
URL: https://github.com/bcrypt-ruby/bcrypt-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/bcrypt-ruby/bcrypt-ruby/archive/refs/tags/v3.1.20.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project for hashing passwords. bcrypt-ruby provides a simple,
humane wrapper for safely handling passwords.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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

pushd .%{gem_instdir}
ln -s %{builddir}/spec .
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bcrypt-doc -f %{oreon_filedir}/rubygem-bcrypt-doc.list

%changelog

%autochangelog
