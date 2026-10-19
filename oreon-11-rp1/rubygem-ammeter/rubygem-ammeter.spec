%global source0_hash 505762f3e49225dc22afbf3fdf3d5d4747924315435e979a9dead1e18da49aad
%global gem_name ammeter
Name: rubygem-%{gem_name}
Version: 1.1.5
Release:        11%{?dist}
Summary:        Write specs for your Rails 3+ generators
License: MIT
URL: https://github.com/alexrothenberg/%{gem_name}
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activerecord)
BuildRequires:  rubygem(haml)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(rspec-rails)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Write specs for your Rails 3+ generators.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec -r haml spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ammeter-doc -f %{oreon_filedir}/rubygem-ammeter-doc.list

%changelog

%autochangelog
