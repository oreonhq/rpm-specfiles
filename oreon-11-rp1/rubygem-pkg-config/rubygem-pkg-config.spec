%global source0_hash 33f9f81c5322983d22b439b8b672f27777b406fea23bfec74ff14bbeb42ec733
%global	gem_name	pkg-config
%undefine	__brp_mangle_shebangs
Summary:        A pkg-config implementation by Ruby
Name:		rubygem-%{gem_name}
Version:	1.6.5
Release:        2%{?dist}
License:	LGPL-2.0-or-later
URL:		http://github.com/rcairo/pkg-config
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	rubygem-pkg-config-1.4.4-cflags-result-sort.patch
Requires:	ruby(release)
Requires:	rubygems
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This gem contains a pkg-config implementation by Ruby

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1

%build

gem build ./%{gem_name}-%{version}.gemspec
%gem_install
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}/%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby test/run.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pkg-config-doc -f %{oreon_filedir}/rubygem-pkg-config-doc.list

%changelog

%autochangelog
