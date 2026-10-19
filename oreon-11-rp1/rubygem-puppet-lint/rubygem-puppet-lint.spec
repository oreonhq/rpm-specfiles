%global source0_hash aa0f5964b111481272f90b7c2fabc0263fc7ef9c935c9dfb47648efeaa3e79d1
%global gem_name puppet-lint
Name: rubygem-%{gem_name}
Version: 4.3.0
Release:        1%{?dist}
Summary:        Ensure your Puppet manifests conform with the Puppetlabs style guide
License: MIT
URL: https://github.com/puppetlabs/puppet-lint/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  puppet-lint-issue225-ruby34-backtrace-formatting-change.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(rspec-its)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Checks your Puppet manifests against the Puppetlabs
style guide and alerts you to any discrepancies.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

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

pushd .%{gem_instdir}
COVERAGE=no rspec spec/unit
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-puppet-lint-doc -f %{oreon_filedir}/rubygem-puppet-lint-doc.list

%changelog

%autochangelog
