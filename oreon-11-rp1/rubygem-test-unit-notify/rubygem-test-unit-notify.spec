%global source0_hash db33d37c32c40f209b8c379b1fee2fb0696a1179ef2b7ce80e358f2f5013fbb7

%global	gem_name	test-unit-notify
%if 0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif

Summary:	Test::Unit::Notify - A test result notify extension for Test::Unit
Name:		rubygem-%{gem_name}
Version:	1.0.4
Release:	23%{?dist}
# https://github.com/test-unit/test-unit-notify/issues/2
# https://cutter.osdn.jp/reference/readme.html
# LGPL-2.1-or-later: overall
# LGPL-3.0-or-later OR GFDL-1.3-or-later OR CC-BY-SA-3.0:
#      kinotan icons (data/icons/kinotan)
# SPDX confirmed
License:	LGPL-2.1-or-later AND (LGPL-3.0-or-later OR GFDL-1.3-or-later OR CC-BY-SA-3.0)
URL:		https://test-unit.github.io/#test-unit-notify
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	https://cutter.osdn.jp/reference/readme.html

Requires:	ruby(release)
BuildRequires:	ruby(release)
Requires:	ruby(rubygems) 
BuildRequires:	rubygems-devel 
BuildArch:	noarch

%description
Test::Unit::Notify - A test result notify extension for Test::Unit.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -p1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

# Permission
find . -type f -print0 | xargs --null chmod go-w

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
cp -p %SOURCE1 %{buildroot}%{gem_instdir}/kinotan-readme.html

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -f  \
	Gemfile \
	Rakefile \
	.yardopts \
	%{nil}

# No test suite available currently

%files
%dir	%{gem_instdir}
%{gem_instdir}/lib/
%{gem_instdir}/data/
%{gem_spec}

%license	%{gem_instdir}/README.md
%license	%{gem_instdir}/kinotan-readme.html
%doc	%{gem_instdir}/doc/

%files doc
%doc	%{gem_docdir}/
%doc	%{gem_instdir}/screenshot/

%changelog
%autochangelog
