%global source0_hash 97da1c55aa3e14850e773c3638974b836ec3dd1095b70da3e41f903dac020113
%global gem_name uuid
Name:           rubygem-%{gem_name}
Version:        2.3.7
Release:        25%{?dist}
Summary:        UUID generator based on RFC 4122
License:        LicenseRef-Callaway-MIT OR LicenseRef-Callaway-CC-BY-SA
URL:            http://github.com/assaf/uuid
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         %{name}-tool.patch
Patch1:         %{name}-file_exists_deprecation.patch
Patch2:         %{gem_name}-pr61-mocha-2.0-compat.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(macaddr)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
UUID generator for producing universally unique identifiers based on RFC 4122
(http://www.ietf.org/rfc/rfc4122.txt).

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
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
sed -i -e '1s,.*,#!/usr/bin/ruby,' bin/uuid

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
mv .%{_bindir}/uuid \
        %{buildroot}%{_bindir}/uuid.rb
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i -e "s,'mocha','mocha/setup'," test/*.rb
ruby -Ilib:test -e 'Dir.glob "./test/*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-uuid-doc -f %{oreon_filedir}/rubygem-uuid-doc.list

%changelog

%autochangelog
