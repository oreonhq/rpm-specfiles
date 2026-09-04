%global source0_hash 077ac92cc16efc5904eb90492a18153b5e6ca5398046d8a249a7c96a9ea24ae6

# Generated from vcr-1.10.0.gem by gem2rpm -*- rpm-spec -*-
%define gem_name vcr

Summary: Record test suite HTTP interactions and replay during future test runs
Name: rubygem-%{gem_name}
Version: 6.4.0
Release: 1%{?dist}
License: MIT
URL: http://github.com/myronmarston/vcr
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
VCR provides a simple API to record and replay your test suite's HTTP
interactions.  It works with a variety of HTTP client libraries, HTTP stubbing
libraries and testing frameworks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_docdir}
%{gem_cache}
%{gem_spec}

%changelog
%autochangelog
