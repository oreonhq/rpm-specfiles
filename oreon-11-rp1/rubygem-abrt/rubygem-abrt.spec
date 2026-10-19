%global source0_hash 6a97058583b091ad62d00ef18cc0b77e44ca7d20729d6f9fb40a01a41fd18735
%global source1_hash 18043e1d18329842e8ad3e8ac0ae1ca026093148aa833502f36b824c72fc01fd
%global gem_name abrt
Name: rubygem-%{gem_name}
Version: 0.5.0
Release:        2%{?dist}
Summary:        ABRT support for Ruby
License: MIT
URL: http://github.com/voxik/abrt-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/voxik/abrt-ruby/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}-spec.tar.gz
Requires: libreport-filesystem
Requires: %{_bindir}/logger
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Provides ABRT reporting support for libraries/applications written using Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_sysconfdir}/libreport/events.d/
cp -a .%{gem_instdir}/config/ruby_event.conf %{buildroot}%{_sysconfdir}/libreport/events.d/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

true
%files -f %{oreon_filedir}/main.list
%files -n rubygem-abrt-doc -f %{oreon_filedir}/rubygem-abrt-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-2
- Import
