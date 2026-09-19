%global source0_hash 6383ce39c5eed7f529a20fcaba404085c7870f0c9bdb3ff6f9e2a15643c26a59

%global	gem_name	native-package-installer

Name:		rubygem-%{gem_name}
Version:	1.1.9
Release:	6%{?dist}
Summary:	Native packages installation helper

# SPDX confirmed
License:	LGPL-3.0-or-later
URL:		https://github.com/ruby-gnome/native-package-installer
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-tests.tar.gz
# Source1 is created by bash %%SOURCE2
Source2:	%{gem_name}-create-missing-files.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-rr)

BuildArch:		noarch

%description
Users need to install native packages to install an extension library
that depends on native packages. It bores users because users need to
install native packages and an extension library separately.
native-package-installer helps to install native packages on "gem install".
Users can install both native packages and an extension library by one action,
"gem install".

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch

%description	doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install
cp -a %{gem_name}-%{version}/test ./%{gem_instdir}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby -Ilib:.:test test/run-test.rb
popd

%files
%license	%{gem_instdir}/doc/text/*gpl*txt
%dir	%{gem_instdir}
%dir	%{gem_instdir}/doc
%dir	%{gem_instdir}/doc/text
%doc	%{gem_instdir}/doc/text/*.md
%doc	%{gem_instdir}/README.md

%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
