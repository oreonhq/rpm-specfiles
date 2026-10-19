%global source0_hash fbb41b6b22750791a4304f0a0aeea3dd837668892117f49c4caf2e8e0f4e792f
%global	gem_name	native-package-installer
Name:		rubygem-%{gem_name}
Version:	1.1.9
Release:        6%{?dist}
Summary:        Native packages installation helper
License:	LGPL-3.0-or-later
URL:		https://github.com/ruby-gnome/native-package-installer
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-tests.tar.gz
Source2:	%{gem_name}-create-missing-files.sh
BuildArch:		noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-rr)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:.:test test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-native-package-installer-doc -f %{oreon_filedir}/rubygem-native-package-installer-doc.list

%changelog

%autochangelog
