%global source0_hash ce3eb9a45cfcb0a068291e0cb1169cd34c47b77c8b29a586c4ad5544e6e88064

# Generated from vcr-1.10.0.gem by gem2rpm -*- rpm-spec -*-
%define gem_name vcr

Summary: Record test suite HTTP interactions and replay during future test runs
Name: rubygem-%{gem_name}
Version: 2.3.0
Release: 26%{?dist}
License: MIT
URL: http://github.com/myronmarston/vcr
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
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
