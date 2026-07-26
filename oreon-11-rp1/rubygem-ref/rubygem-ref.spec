%global source0_hash b9cf79889f1f6d28c4020745f7426c43c93fe15d1b5eb6186a6318cd14e3c069

# Generated from ref-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ref

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 20%{?dist}
Summary: Library that implements weak, soft, and strong references in Ruby
License: MIT
URL: http://github.com/ruby-concurrency/ref
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby-concurrency/ref.git && cd ref
# git checkout v2.0.0 && tar czvf ref-2.0.0-tests.tgz ./spec/
Source1: ref-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch
%if 0%{?rhel} == 7
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Library that implements weak, soft, and strong references in Ruby that work
across multiple runtimes (MRI,Jruby and Rubinius). Also includes
implementation of maps/hashes that use references and a reference queue.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xf %{SOURCE1}

# We don't care about coverage.
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
sed -i '/simplecov/ s/^/#/' spec/spec_helper.rb
sed -i '/SimpleCov/,/^end$/ s/^/#/' spec/spec_helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT_LICENSE
%exclude %{gem_instdir}/ext
# We don't rebuild Jave extension ATM, so exclude it.
%exclude %{gem_libdir}/*.jar
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
