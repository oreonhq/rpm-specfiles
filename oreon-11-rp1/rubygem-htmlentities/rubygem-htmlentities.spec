%global source0_hash bbafbdf69f2eca9262be4efef7e43e6a1de54c95eb600f26984f71d2fe96c5c3
%global	gem_name		htmlentities
%global	test_version	4.4.1
Summary:        A module for encoding and decoding (X)HTML entities
Name:		rubygem-%{gem_name}
Version:	4.4.2
Release:        1%{?dist}
License:	MIT
URL:		https://github.com/threedaymonk/htmlentities
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{test_version}-tests.tar.gz
Source2:	htmlentities-create-missing-files.sh
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
HTMLEntities is a simple library to facilitate encoding and 
decoding of named (&yacute; and so on) or numerical (&#123; or &#x12a;) 
entities in HTML and XHTML documents.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(rubygems)
%description	doc
This package contains documentation for %{name}.

%package	-n ruby-%{gem_name}
Summary:	Non-Gem support for %{gem_name}
Requires:	%{name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
%description	-n ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1

mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -a %{gem_name}-%{test_version}/spec ./%{gem_instdir}
pushd ./%{gem_instdir}/
rspec spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-htmlentities-doc -f %{oreon_filedir}/rubygem-htmlentities-doc.list
%files -n ruby-htmlentities -f %{oreon_filedir}/ruby-htmlentities.list

%changelog

%autochangelog
