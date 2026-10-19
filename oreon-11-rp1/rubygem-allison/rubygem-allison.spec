%global source0_hash d39167373aa562f5ac54f737aa9ef0e72e62504786b433c713b8ff21b2738bb5
%global	gem_name	allison
Summary:        A modern, pretty RDoc template
Name:		rubygem-%{gem_name}
Version:	2.0.3
Release:        35%{?dist}
License:	AFL-3.0
URL:		http://github.com/fauna/allison/tree/master
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
%{summary}.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/
rm -rf %{buildroot}%{gem_dir}/bin
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}/
rm -f \
	Manifest \
	%{gem_name}.gemspec \
	%{nil}
popd
rm -f %{buildroot}%{gem_instdir}/%{gem_name}.gemspec
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-allison-doc -f %{oreon_filedir}/rubygem-allison-doc.list

%changelog

%autochangelog
