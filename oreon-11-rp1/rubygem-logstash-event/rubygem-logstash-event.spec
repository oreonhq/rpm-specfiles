%global source0_hash 89a7dc60fac67070a5f60ba07409e541b09cb58906c391e90cb74b9f217467ae

%global gem_name logstash-event

Name:           rubygem-%{gem_name}
Version:        1.2.02
Release:        25%{?dist}
Summary:        Library that contains the classes required to create LogStash events

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/logstash/logstash
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  rubygems-devel
# for tests:
# BuildRequires: rubygem(rspec)
# BuildRequires: rubygem(insist) = 1.0.0
# missing in gemspec
Requires:       rubygem(json)
%if 0%{?fedora} && 0%{?fedora} <= 20 || 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
rubygem-%{gem_name} contains the classes required to create LogStash events
(combination of timestamp in ISO8601 format and message in any format) and their
serialization to json.

%{gem_name} rubygem is part of LogStash project, http://logstash.net/.

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

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Dependencies for test suite not in Fedora/EPEL yet
#%%check
#pushd .%%{gem_instdir}
#rspec -Ilib spec/event.rb
#popd

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
%autochangelog
