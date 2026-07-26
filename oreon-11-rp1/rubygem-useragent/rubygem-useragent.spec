%global source0_hash 724f1d6bc5be48aec3408d58573264e8b26812fda4a8699031138ba0b85c69be

# Generated from useragent-0.16.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name useragent

Name: rubygem-%{gem_name}
Version: 0.16.11
Release: 5%{?dist}
Summary: HTTP User Agent parser
License: MIT
URL: https://github.com/gshutler/useragent
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/gshutler/useragent.git && cd useragent
# git archive -v -o useragent-0.16.11-spec.tar.gz v0.16.11 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: rubygem(ostruct)
BuildArch: noarch

%description
HTTP User Agent parser.

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{builddir}/spec .
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
