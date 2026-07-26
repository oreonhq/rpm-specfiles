%global source0_hash 8b01940eb6672a2ef62e717e87d3b385fa4dcdd547b6c8fa131f39bad7facebe

%global gem_name bcrypt

Name: rubygem-%{gem_name}
Version: 3.1.20
Release: 3%{?dist}
Summary: Wrapper around bcrypt() password hashing algorithm
# ext/mri/* - bcrypt-Solar-Designer
# Non of theses are part of resulting package.
# ext/jruby/* - ISC
# spec/TestBCrypt.java - ISC
License: MIT AND bcrypt-Solar-Designer
URL: https://github.com/bcrypt-ruby/bcrypt-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/bcrypt-ruby/bcrypt-ruby.git && cd bcrypt-ruby
# git archive -v -o bcrypt-3.1.20-specs.tar.gz v3.1.20 spec/
Source1: bcrypt-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
BuildRequires: gcc

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
pushd .%{gem_instdir}
ln -s %{builddir}/spec .
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
