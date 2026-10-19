%global source0_hash c06641e3463532b8a67e50b8a6ae526853c2046307d1bb4423d987ff4b1d66b5
%global _lto_cflags %nil
%undefine _hardened_build
%bcond_without gnutls
%bcond_without ldap
%bcond_with gps
%global upstream_owner    AdaCore
%global upstream_name     aws
%global upstream_version  26.0.0
%global upstream_commit   2e783e32f15f9de271a4ca2de5168bcf37d23fc2
Name:           aws
Epoch:          2
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        The Ada Web Server
License:        (GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception) AND GPL-2.0-or-later WITH GNAT-exception
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        aws-manpages.tar.gz
Patch:          %{name}-use-external-template-parser.patch
Patch:          %{name}-use-external-zlib-library.patch
Patch:          %{name}-use-external-xmlada-library.patch
Patch:          %{name}-set-soname-of-aws-library.patch
Patch:          %{name}-set-soname-of-aws-ssl-library.patch
Patch:          %{name}-link-components-dynamically.patch
Patch:          %{name}-no-symbol-stripping.patch
Patch:          %{name}-no-build-and-install-names.patch
Patch:          %{name}-no-third-party-javascript-source-code.patch
Patch:          %{name}-recommend-mailcap-for-mime-types.patch
Patch:          aws-trust-the-system-trust-store.patch
%if %{with ldap}
%endif
%if %{with gnutls}
%endif
ExclusiveArch:  %{GPRbuild_arches}
%global common_description_en \
AWS is a complete framework to develop Web based applications. The main part \
of the framework is the embedded Web server. This small yet powerful Web \
server can be embedded into your application so your application will be able \
to talk with a standard Web browser.
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  findutils
BuildRequires:  gcc-gnat
BuildRequires:  gnatcoll-core-devel
BuildRequires:  gnutls-devel
BuildRequires:  gprbuild
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  tar
BuildRequires:  templates_parser-devel
BuildRequires:  xmlada-devel
BuildRequires:  zlib-ada-devel
# /oreon:deps
%description %{common_description_en}

#################
## Subpackages ##
#################

%package tools
Summary:        Tools for the Ada Web Server
License:        GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception)
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnutls-devel
Requires:       libgcrypt-devel
%description tools %{common_description_en}

This package contains contains supporting tools for the Ada Web Server.

%package doc
Summary:        Documentation for the Ada Web Server
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception)
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.

%package devel
Summary:        Development files for the Ada Web Server
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       templates_parser-devel
Requires:       xmlada-devel
Requires:       gnatcoll-core-devel
Requires:       zlib-ada-devel
%if %{with gnutls}
Requires:       gnutls-devel
Requires:       libgcrypt-devel
%endif
%if %{with ldap}
Requires:       openldap-devel
%endif
Recommends:     %{name}-tools
Recommends:     %{name}-doc
Recommends:     mailcap
%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the Ada Web Server.

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

# Update some release specific information in the source code. The substitution
# is scoped to a specific line to increase the chance of detecting code changes
# at this point. Sed should exit with exit code 0 if the substitution succeeded
# (using `t`, jump to end of script) or exit with a non-zero exit code if the
# substitution failed (using `q1`, quit with exit code 1).
sed --in-place \
    --expression='34 { s,20\.0,%{upstream_version}, ; t; q1 }' \
    src/core/aws.ads

# Unpack the man pages.
tar -xvf %SOURCE1

# Ignore the templates_parser Git submodule.
rm -rf templates_parser
# Delete the bundled zlib library.
rm -rf include/zlib*

# No silent makefiles.
# Issue: https://github.com/AdaCore/aws/issues/378
find -type f -name "Makefile" \
    | xargs sed --regexp-extended --in-place \
                --expression '/^\.SILENT:/d'

# Convert readme.txt to UTF-8.
mv readme.txt readme.txt.old
iconv --from=ISO-8859-1 --to=UTF-8 readme.txt.old > readme.txt
rm readme.txt.old

# Exclude all third-party Javascript source code with unclear license, the demos
# that depend on it and the readme file that promotes usage of the Javascript
# source code.
rm -rf ./web_elements/javascripts
rm -rf ./web_elements/notebook
rm     ./web_elements/readme.txt

rm -rf ./demos/web_block_ajax
rm -rf ./demos/web_block_ajax_templates
rm -rf ./demos/web_elements
rm -rf ./demos/websockets
rm -rf ./demos/ws_candy

# Exclude demo "soap_hello" as it requires ada2wsdl - a tool not included in the
# ada-tools package as it depends on libadalang - a library not available in
# Fedora.
rm -rf ./demos/soap_hello

# Fix demo "wps". The WWW-root will be ../shared/web_elements instead of
# ../../web_elements after installation. The demo also needs a certificate from
# the testsuite.
cp --preserve=timestamp regtests/0111_sslcfg/cert.pem ./demos/wps

sed --regexp-extended --in-place \
    --expression '/^www_root/ { s,\.\./\.\./web_elements,../shared/web_elements, ; t; q1 }' \
    --expression '/^certificate/ { s,\.\./\.\./regtests/0111_sslcfg/cert.pem,cert.pem, ; t; q1 }' \
    ./demos/wps/wps.ini

# Fix demo "ws". The WWW-root will be ../shared/web_elements instead of
# ../../web_elements after installation.
sed --regexp-extended --in-place \
    --expression '/^www_root/ { s,\.\./\.\./web_elements,../shared/web_elements, ; t; q1 }' \
    ./demos/ws/ws.ini

# Improve instructions for building the demos. The wsdl2aws-tool must know where
# to find the templates.
sed --regexp-extended --in-place \
    --expression '7 { s,\$ make$,$ AWS_TEMPLATE_FILES=${PWD}/shared/wsdl2aws-templates make, ; t; q1 }' \
    ./demos/README

###########
## Build ##
###########

%build

%if %{with ldap}
LDAP=true
%else
LDAP=false
%endif
%if %{with gnutls}
SOCKET=gnutls
SSL_DYNAMIC=false
%else
SOCKET=std
SSL_DYNAMIC=false
%endif
make setup GPRBUILD='gprbuild %{GPRbuild_flags} -XVERSION=%{version}' \
     PYTHON='%python3' ENABLE_SHARED=true DEBUG=false \
     XMLADA=true LAL=false ZLIB=true \
     LDAP=$LDAP SOCKET=$SOCKET SSL_DYNAMIC=$SSL_DYNAMIC
%{make_build} -j1 GPRBUILD='gprbuild %{GPRbuild_flags} -XVERSION=%{version}' \
     LIBRARY_TYPE=relocatable
make -C docs html latexpdf
%install
make install \
     GPRINSTALL='%{GPRinstall} -XVERSION=%{version}' \
     prefix=%{buildroot}%{_prefix}
cp --preserve=timestamps \
   %{_builddir}/%{name}-%{version}/*/release/relocatable/lib/ssl/lib%{name}_ssl.so* \
   %{buildroot}%{_libdir}/
ln --symbolic --force lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
ln --symbolic --force lib%{name}_ssl.so.%{version} %{buildroot}%{_libdir}/lib%{name}_ssl.so
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps --recursive \
   demos/* %{buildroot}%{_pkgdocdir}/examples
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples/shared
rmdir %{buildroot}%{_datadir}/examples
rm -rf %{buildroot}%{_pkgdocdir}/examples/shared/images
rm -rf %{buildroot}%{_pkgdocdir}/examples/shared/templates
rm -rf %{buildroot}%{_pkgdocdir}/examples/shared/web_elements/mime.types
mkdir --parents %{buildroot}%{_mandir}/man1
cp --preserve=timestamps *.1 %{buildroot}%{_mandir}/man1/
%{py3_shebang_fix} %{buildroot}/%{_bindir}/awsascb
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}.gpr
%oreon_autofiles aws-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles aws-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles aws-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aws-tools -f %{oreon_filedir}/aws-tools.list
%files -n aws-doc -f %{oreon_filedir}/aws-doc.list
%files -n aws-devel -f %{oreon_filedir}/aws-devel.list

%changelog

%autochangelog
