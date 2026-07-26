%global source0_hash adcced78492e7366d940c66a1327a85d3ae8c45190f486f545fdaa84cac662f0

%global	githash	79ff51e50bacdf9516e0fa6eda278052c82f8ea5
%global	shorthash	%(c=%{githash}; echo ${c:0:7})
%global	gitdate	Mon, 13 Jul 2015 22:29:10 +0530
%global	tardate	20150713

%global	usegitsource	0

%global	mainver	0.12.6
#%%global	minorver	D%{?tardate}git%{shorthash}
#%%global	prerelease	1

%global	baserelease	9

Name:		wkhtmltopdf
Version:	%{mainver}
Release:	%{?prerelease:0.}%{baserelease}%{?minorver:.%minorver}%{?dist}
Summary:	Simple shell utility to convert html to pdf

# overall	LGPL-3.0-or-later
# docs/js/foundation.min.js and some other *.js		MIT
# docs/js/vendor/modernizr.js	says "MIT and BSD",  choose "MIT" for now
# docs/libwkhtmltox/jquery.js	MIT OR GPL-2.0-only
#
# SPDX confirmed
License:	LGPL-3.0-or-later
URL:		http://wkhtmltopdf.org/
#Source0:	https://github.com/%{name}/%{name}/archive/%{githash}/%{name}-%{mainver}-D%{tardate}git%{shorthash}.tar.gz
Source0:	https://github.com/%{name}/%{name}/archive/%{mainver}/%{name}-%{mainver}.tar.gz

BuildRequires:	make
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtxmlpatterns-devel
BuildRequires:	qt5-qtsvg-devel

%description
Simple shell utility to convert html to pdf using the webkit
rendering engine, and qt. 

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation for %{name}
License:	LGPL-3.0-or-later AND MIT AND (MIT OR GPL-2.0-only)
Requires:	%{name} = %{version}
BuildArch:	noarch

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usegitsource} >= 1
%setup -q -c -T -a 0
cd %{name}-*/
%else
%setup -q -n %{name}-%{mainver}%{?minorver:_%minorver}
%endif
# libdir handling.. better handling needed
sed -i.lib -e \
	'/INSTALLBASE/s|lib|%{_lib}|' \
	src/lib/lib.pro

# Remove BOM
sed -i.bom -e 's|\xEF\xBB\xBF||' AUTHORS
touch -r AUTHORS{.bom,}
rm -f AUTHORS.bom

%build
%if 0%{?usegitsource} >= 1
cd %{name}-*/
%endif
%{qmake_qt5}
make %{_smp_mflags}

%install
%if 0%{?usegitsource} >= 1
cd %{name}-*/
cp -a [A-Z]* examples/ docs/ ..
%endif

make install \
	INSTALL_ROOT=%{buildroot}%{_prefix}

%ldconfig_scriptlets

%files
%doc	AUTHORS
%license	LICENSE
%doc	CHANGELOG.md
%doc	CHANGELOG-OLD
%doc	README.md

%{_libdir}/libwkhtmltox.so.0*
%{_bindir}/wkhtmltoimage
%{_bindir}/wkhtmltopdf

%{_mandir}/man1/wkhtmltoimage.1*
%{_mandir}/man1/wkhtmltopdf.1*

%files devel
%doc    examples/
%{_libdir}/libwkhtmltox.so
%{_includedir}/wkhtmltox/

%files doc
%doc	docs/

%changelog
%autochangelog
