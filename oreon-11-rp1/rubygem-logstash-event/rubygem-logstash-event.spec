%global source0_hash 89a7dc60fac67070a5f60ba07409e541b09cb58906c391e90cb74b9f217467ae
%global gem_name logstash-event
Name:           rubygem-%{gem_name}
Version:        1.2.02
Release:        1%{?dist}
Summary:        Library that contains the classes required to create LogStash events
License:        Apache-2.0
URL:            https://github.com/logstash/logstash
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:      noarch
Requires:       rubygem(json)
# oreon:deps
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-logstash-event-doc -f %{oreon_filedir}/rubygem-logstash-event-doc.list

%changelog

%autochangelog
