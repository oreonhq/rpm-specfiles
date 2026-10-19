%global source0_hash 4f7983a69720d6cc3427a137b31b0737b63033d96d80d8dbb4ad360e75abf325
%bcond_with tests
%global gem_name drake
Name:           rubygem-%{gem_name}
Version:        0.9.2.0.3.1
Release:        1%{?dist}
Summary:        A branch of Rake supporting automatic parallelizing of tasks
License:        MIT
URL:            http://quix.github.io/rake/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:      noarch
%if %with tests
%endif
Requires:       ruby(release) >= 1.8
Requires:       rubygem(comp_tree)
Requires:       rubygems
Provides:       rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  rubygem(comp_tree)
BuildRequires:  rubygem(flexmock)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(session)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Drake is an auto-parallelizing branch of Rake, a Make-like program
implemented in Ruby. Tasks and dependencies are specified in standard
Ruby syntax.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby >%{gem_name}.gemspec

# From lib/rake.rb
%gemspec_add_dep -g logger -s %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%if %with tests
%check

./bin/drake test
%endif
%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}
chmod 644 %{buildroot}%{gem_instdir}/lib/rake/ruby182_test_unit_fix.rb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-drake-doc -f %{oreon_filedir}/rubygem-drake-doc.list

%changelog

%autochangelog
