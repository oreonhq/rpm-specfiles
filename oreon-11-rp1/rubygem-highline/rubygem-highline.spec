%global source0_hash ca18b218fd581b1fae832f89bfeaf2b34d3a93429c44fd4411042ffce286f009
%global gem_name highline
Summary:        HighLine is a high-level command-line IO library
Name: rubygem-%{gem_name}
Version: 3.0.1
Release:        1%{?dist}
License: GPL-2.0-only or Ruby
URL: https://github.com/JEG2/highline
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(simplecov)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A high-level IO library that provides validation, type conversion, and more
for command-line interfaces. HighLine also includes a complete menu system
that can crank out anything from simple list selection to complete shells
with just minutes of work.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_instdir}/{examples,lib}/ -type f -name '*.rb' -exec \
    sed -i -e 's|/usr/local/bin/ruby|/usr/bin/ruby|' '{}' \;
find %{buildroot}%{gem_instdir}/ -type f -iname '.*' -exec rm -f '{}' \;
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -rf %{buildroot}%{gem_instdir}/.github
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar xfj %{SOURCE1}
ruby -Ilib:test test/test_*.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-highline-doc -f %{oreon_filedir}/rubygem-highline-doc.list

%changelog

%autochangelog
