%global source0_hash 336b753676d6117cad9301fac7e91dab4228f747d4e7179891ad3a163c64e2ed
%global gem_name optimist
%bcond check 0
Name:           rubygem-%{gem_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Commandline option parser for Ruby
License:        MIT
URL:            https://rubygems.org/gems/optimist
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Patch0:         optimist-pr140-minitest-5_20-compat.patch
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(chronic)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

ruby -Ilib:test -e '$0="workaround"; Dir.glob "./test/**/*_test.rb", &method(:require)'
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-optimist-doc -f %{oreon_filedir}/rubygem-optimist-doc.list

%changelog

%autochangelog
