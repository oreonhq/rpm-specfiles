%global source0_hash d54610a14c788fa24691172d4939a33fc92b866b88a9fed1405743453c9d0022

# Generated from gem2rpm-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gem2rpm

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 2%{?dist}
Summary: Generate rpm specfiles from gems
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/fedora-ruby/gem2rpm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/fedora-ruby/gem2rpm.git && cd gem2rpm
# git checkout v2.0.0 && tar czvf gem2rpm-2.0.0-tests.tar.gz test/
Source1: %{gem_name}-%{version}-tests.tar.gz
Requires: %{_bindir}/rpmdev-packager
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/rpmdev-packager
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildArch: noarch

%description
Generate source rpms and rpm spec files from a Ruby Gem. The spec file
tries to follow the gem as closely as possible, and be compliant with the
Fedora rubygem packaging guidelines.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

TEST_GEM2RPM_LOCAL=1 ruby -Itest -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%{_bindir}/gem2rpm
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/templates
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
