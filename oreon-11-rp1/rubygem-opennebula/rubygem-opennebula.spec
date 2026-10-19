%global source0_hash 4612319f543128d057995332d8f49a37116025766b7854e2c743f704965040d2
%global gem_name opennebula
Name:           rubygem-%{gem_name}
Version:        6.4.2
Release:        1%{?dist}
Summary:        OpenNebula Client API
License:        Apache-2.0
URL:            http://opennebula.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Libraries needed to talk to OpenNebula.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# bigdecimal is in independent package in Fedora.
%gemspec_add_dep -g bigdecimal
# rexml extracted into independent gem
%gemspec_add_dep -g rexml

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-opennebula-doc -f %{oreon_filedir}/rubygem-opennebula-doc.list

%changelog

%autochangelog
