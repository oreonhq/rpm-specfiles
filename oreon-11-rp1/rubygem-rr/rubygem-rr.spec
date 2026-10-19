%global source1_hash b0dda83de6713d631a3bd5782f974dfb736639fcc5cb1f9eae029a696f7ce05f
%global source0_hash b77a801bd19877b636004fb11c2903b50788063b6935867efd5f30a2163a2fd9
%global gem_name rr
Name: rubygem-%{gem_name}
Version: 1.2.1
Release:        1%{?dist}
Summary:        RR is a test double framework with a terse syntax
License: MIT
URL: https://rr.github.io/rr
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rr/rr/archive/refs/tags/v1.2.1.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-rr)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RR is a test double framework that features a rich selection of double
techniques and a terse syntax.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar xvzf %{SOURCE1}
ruby test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rr-doc -f %{oreon_filedir}/rubygem-rr-doc.list

%changelog

%autochangelog
