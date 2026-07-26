%global source0_hash bc68802148f5e9cf721c3e27e8522a002dfe05f7ce626420d891bf00e5d08125

%global gem_name rspec-pending_for

Name:           rubygem-%{gem_name}
Version:        0.1.16
Release:        11%{?dist}
Summary:        Mark specs pending or skipped for specific Ruby engine

License:        MIT
URL:            https://github.com/pboling/rspec-pending_for
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/pboling/rspec-pending_for && cd rspec-pending_for
# git checkout v0.1.16
# tar -czf rubygem-rspec-pending_for-0.1.16-specs.tgz spec/
Source1:        %{name}-%{version}-specs.tgz

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(ruby_engine) >= 1.0
BuildRequires:  rubygem(ruby_version) >= 1.0
BuildRequires:  rubygem(simplecov)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(rubygems)
Requires:       rubygem(rspec-core)
Requires:       rubygem(ruby_engine) >= 1.0
Requires:       rubygem(ruby_engine) < 2
Requires:       rubygem(ruby_version) >= 1.0
Requires:       rubygem(ruby_version) < 2
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations.
%if 0%{?rhel} && 0%{?rhel} <= 7
Note, skip_for() function is not available in rspec <= 2.
%endif

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
tar -xzf %{SOURCE1}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
cp -a spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
rspec -Ilib -rspec_helper spec
rm -rf spec/
popd

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
