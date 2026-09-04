%global source0_hash aec0cf592053cd6e07c13c1ef94c440aba705f22eb1ee767b39631f2760124d7

%global gem_name uuid

Name:           rubygem-%{gem_name}
Version:        2.3.9
Release:        1%{?dist}
Summary:        UUID generator based on RFC 4122

# Automatically converted from old format: MIT or CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-MIT OR LicenseRef-Callaway-CC-BY-SA
URL:            http://github.com/assaf/uuid
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/assaf/uuid/pull/39
Patch0:         %{name}-tool.patch
# https://github.com/assaf/uuid/pull/36
# Needed for ruby3.2, which removes File.exists? deprecated since ruby 2.1
Patch1:         %{name}-file_exists_deprecation.patch
# https://github.com/assaf/uuid/pull/61
# Compatibility for mocha 2.0
Patch2:         %{gem_name}-pr61-mocha-2.0-compat.patch

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(macaddr)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(test-unit)
%if 0%{?fedora} && 0%{?fedora} <= 20 || 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(macaddr) >= 1.0
Requires:       rubygem(macaddr) < 2
Provides:       rubygem(%{gem_name}) = %{version}
%endif

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
# rename to fix conflict with uuid package
mv .%{_bindir}/uuid \
        %{buildroot}%{_bindir}/uuid.rb

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# https://github.com/assaf/uuid/issues/43
sed -i -e "s,'mocha','mocha/setup'," test/*.rb
ruby -Ilib:test -e 'Dir.glob "./test/*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}/
%dir %{gem_instdir}/bin/
%license %{gem_instdir}/MIT-LICENSE
%{_bindir}/uuid.rb
%{gem_instdir}/bin/uuid
%{gem_libdir}/
%{gem_spec}
%{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/bin/rake
%exclude %{gem_instdir}/bin/yard
%exclude %{gem_instdir}/bin/yardoc
%exclude %{gem_instdir}/bin/yri
%exclude %{gem_instdir}/test/
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
