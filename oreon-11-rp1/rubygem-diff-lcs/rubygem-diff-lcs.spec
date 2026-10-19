%global source0_hash 708a5d52ec2945b50f8f53a181174aa1ef2c496edf81c05957fe956dabb363d5
%global gem_name diff-lcs
%{!?_with_bootstrap: %global bootstrap 0}
Name: rubygem-%{gem_name}
Version: 2.0.0
Release:        1%{?dist}
Summary:        Provide a list of changes between two sequenced collections
License: MIT OR Artistic-2.0 OR GPL-2.0-or-later
URL: https://github.com/halostatue/diff-lcs
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if ! 0%{?bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version}

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
sed -i 's|^#!.*|#!/usr/bin/ruby|' %{buildroot}%{gem_instdir}/bin/{htmldiff,ldiff}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if ! 0%{?bootstrap}
%check

pushd .%{gem_instdir}
rspec spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-diff-lcs-doc -f %{oreon_filedir}/rubygem-diff-lcs-doc.list

%changelog

%autochangelog
