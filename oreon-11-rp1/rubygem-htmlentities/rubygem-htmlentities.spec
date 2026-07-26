%global source0_hash 4c3b7c3b7fcfcbe75cca0a97b4b08159a03b434cfb0aafda72537b7170fad3f2

# Generated from htmlentities-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name		htmlentities
%global	test_version	4.4.1

# Some functions removed on 4.2.4. Please don't upgrade this rpm
# to 4.3.0+ on F-14-

Summary:	A module for encoding and decoding (X)HTML entities
Name:		rubygem-%{gem_name}
Version:	4.4.2
Release:	2%{?dist}
License:	MIT
URL:		https://github.com/threedaymonk/htmlentities
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{test_version}-tests.tar.gz
# Source1 is created by bash %%SOURCE2 %%test_version
Source2:	htmlentities-create-missing-files.sh

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	rubygems-devel
BuildRequires:	rubygem(rspec)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
HTMLEntities is a simple library to facilitate encoding and 
decoding of named (&yacute; and so on) or numerical (&#123; or &#x12a;) 
entities in HTML and XHTML documents.

%package	doc
Summary:	Documentation for %{name}
# Directory ownership issue
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

%check
cp -a %{gem_name}-%{test_version}/spec ./%{gem_instdir}
pushd ./%{gem_instdir}/

rspec spec

%files
%license	%{gem_instdir}/COPYING.txt
%dir	%{gem_instdir}
%doc	%{gem_instdir}/History.txt

%{gem_libdir}/
%{gem_spec}

%files	doc
%{gem_docdir}/

%changelog
%autochangelog
