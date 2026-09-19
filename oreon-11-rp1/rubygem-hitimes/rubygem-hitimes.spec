%global source0_hash 199e84fbf73038ef3f95efe464ff6d28d321d18f5b0fe77b2e253383bdf8aa69

# Generated from hitimes-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hitimes

Name: rubygem-%{gem_name}
Version: 3.0.0
Release: 4%{?dist}
Summary: A fast, high resolution timer library for recording performance metrics
License: ISC
URL: http://github.com/copiousfreetime/hitimes
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/copiousfreetime/hitimes.git && cd hitimes
# git archive -v -o hitimes-3.0.0-spec.tar.gz v3.0.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Hitimes is a fast, high resolution timer library for recording performance
metrics. It uses the internal ruby `Process::clock_gettime()` to get the highest
granularity time increment possible. Generally this is nanosecond resolution, or
whatever the hardware in the CPU supports.

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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

# We don't have minitest-focus in Fedora, but it is likely not needed at all.
sed -i '/minitest\/focus/ s/focus/autorun/' spec/spec_helper.rb

ruby -Ilib:spec -e 'Dir.glob "./spec/*spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/hitimes.gemspec

%changelog
%autochangelog
