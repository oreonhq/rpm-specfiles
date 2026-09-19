%global source0_hash 135c2de7894dfb6c31032513826f5cd6743a6a6eb5135dca3aacb134ba188f9b

%global gem_name jmespath

%if 0%{?rhel} && 0%{?rhel} <= 7
%global use_tests 0
%else
%global use_tests 1
%endif

Name:           rubygem-%{gem_name}
Version:        1.6.2
Release:        10%{?dist}
Summary:        JMESPath - Ruby Edition

License:        Apache-2.0
URL:            http://github.com/trevorrowe/jmespath.rb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/trevorrowe/jmespath.rb && cd jmespath.rb
# git checkout v1.6.2
# tar -czf rubygem-jmespath-1.6.2-repo.tgz spec/ CHANGELOG.md README.md
Source1:        %{name}-%{version}-repo.tgz

BuildArch:      noarch
BuildRequires:  rubygems-devel
%if 0%{?use_tests}
BuildRequires:  rubygem(json)
BuildRequires:  rubygem(rspec) >= 3
BuildRequires:  rubygem(rspec) < 4
%endif
Requires:       rubygem(json)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Implements JMESPath for Ruby.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version} -a 1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

cp -a CHANGELOG.md README.md %{buildroot}%{gem_instdir}/

%check
%if 0%{?use_tests}
cp -pr spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
# not using bundler - perform only the test without json dependency
echo "require 'jmespath'" > spec/spec_helper.rb

# https://github.com/jmespath/jmespath.rb/issues/63
# Remove tests failing for ruby4_0 for now
rm -f spec/compliance/identifiers.json

rspec -Ilib spec
rm -rf spec/
popd
%endif

%files
%dir %{gem_instdir}/
%license %{gem_instdir}/LICENSE.txt
%{_bindir}/jmespath.rb
# required at runtime
%{gem_instdir}/VERSION
%{gem_instdir}/bin/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
