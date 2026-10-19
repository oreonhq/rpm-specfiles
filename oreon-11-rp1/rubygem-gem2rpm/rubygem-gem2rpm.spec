%global source1_hash 369aecf20093f04897c564cb6ebe4a70cbf1ab0e7381123d59bea72660e3931d
%global source0_hash efb1f5a29e084414ab2d86ac80aff1ea5b39f650cfb8dbe12a0e61932962608b
%global gem_name gem2rpm
Name: rubygem-%{gem_name}
Version: 2.0.0
Release:        1%{?dist}
Summary:        Generate rpm specfiles from gems
License: GPL-2.0-or-later
URL: https://github.com/fedora-ruby/gem2rpm
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/fedora-ruby/gem2rpm/archive/refs/tags/v2.0.0.tar.gz
Requires: %{_bindir}/rpmdev-packager
BuildArch: noarch
# oreon:deps
BuildRequires:  //bin/rpmdev-packager
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/test .
TEST_GEM2RPM_LOCAL=1 ruby -Itest -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gem2rpm-doc -f %{oreon_filedir}/rubygem-gem2rpm-doc.list

%changelog

%autochangelog
