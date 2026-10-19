%global source1_hash 7464700c3a8478a43ca0a91ba125aafed05f8548c4973d088845982a963d7543
%global source0_hash 10d76e070c86b12fec74b6a9515fd1940f4459198b991342d0a7897d86c372fe
%global gem_name loofah
Name: rubygem-%{gem_name}
Version: 2.22.0
Release:        1%{?dist}
Summary:        Manipulate and transform HTML/XML documents and fragments
License: MIT
URL: https://github.com/flavorjones/loofah
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/flavorjones/loofah/archive/refs/tags/v2.22.0.tar.gz
Patch0:  %{gem_name}-2.22.0-minitest6.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(crass)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Loofah is a general library for manipulating and transforming HTML/XML documents
and fragments, built on top of Nokogiri. Loofah also includes some HTML
sanitizers based on `html5lib`'s safelist, which are a specific application of
the general transformation functionality.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd %{_builddir}
%patch -P0 -p1
)

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
cp -a %{_builddir}/test .
ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-loofah-doc -f %{oreon_filedir}/rubygem-loofah-doc.list

%changelog

%autochangelog
