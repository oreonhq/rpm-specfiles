%global source0_hash 2274261bd3bceb18d815197349031d99fe236649644007a8cb7987280af10d7b
Name:           scapy
Version:        2.7.0
Release:        1%{?dist}
Summary:        Interactive packet manipulation tool and network scanner
%global         gituser         secdev
%global         gitname         scapy
%global         gitdate         20251225
%global         commit          40fc5ecf9e69e9bd76664d63ae133d4973fcf81b
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         giturl          https://github.com/%{gituser}/%{gitname}
License:        GPL-2.0-only
URL:            https://scapy.net/
VCS:            git:%{giturl}
Source0:        https://github.com/secdev/scapy/archive/v2.7.0.tar.gz#/scapy-2.7.0.tar.gz
Patch0:         scapy-2.7.0-rhel9.patch
%global         common_desc %{expand:
Scapy is a powerful interactive packet manipulation program built on top
of the Python interpreter. It can be used to forge or decode packets of
a wide number of protocols, send them over the wire, capture them, match
requests and replies, and much more.}
%bcond_with        doc
BuildArch:      noarch
%if %{with doc}
%endif
Recommends:     tcpdump
Recommends:     wireshark-cli
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.0.0
Requires:       python3-scapy = %{version}-%{release}
# /oreon:deps
%package -n       python3-scapy+cli
Summary:        Metapackage for python3-scapy cli extras
Requires:       python3-scapy = %{version}-%{release}
Provides:       python3dist(scapy[cli]) = %{version}-%{release}

%description -n python3-scapy+cli
Metapackage for python3-scapy cli extras.

%package -n       python3-scapy+all
Summary:        Metapackage for python3-scapy all extras
Requires:       python3-scapy = %{version}-%{release}
Requires:       python3dist(cryptography) >= 2.0
Provides:       python3dist(scapy[all]) = %{version}-%{release}

%description -n python3-scapy+all
Metapackage for python3-scapy all extras.

%package -n       python3-scapy+doc
Summary:        Metapackage for python3-scapy doc extras
Requires:       python3-scapy = %{version}-%{release}
Requires:       python3dist(cryptography) >= 2.0
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(sphinx-rtd-theme) >= 1.3.0
Requires:       python3dist(tox) >= 3.0.0
Provides:       python3dist(scapy[doc]) = %{version}-%{release}

%description -n python3-scapy+doc
Metapackage for python3-scapy doc extras.

%description %{common_desc}

%package -n python%{python3_pkgversion}-%{name}
Summary:        Interactive packet manipulation tool and network scanner
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Provides:       %{name} = %{version}-%{release}
Recommends:     PyX
Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     ipython3
%description -n python%{python3_pkgversion}-%{name}
%{common_desc}

%if %{with doc}
%package doc
Summary:        Interactive packet manipulation tool and network scanner
License:        CC-BY-NC-SA-2.5
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%description doc
%{common_desc}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 -n %{name}-%{version}

# Remove shebang
# https://github.com/secdev/scapy/pull/2332
SHEBANGS=$(find ./scapy -name '*.py' -print | xargs grep -l -e '^#!.*env python')
for FILE in $SHEBANGS ; do
    sed -i.orig -e 1d "${FILE}"
    touch -r "${FILE}.orig" "${FILE}"
    rm "${FILE}.orig"
done

%build

%pyproject_wheel
%if %{with doc}
make -C doc/scapy html BUILDDIR=_build_doc SPHINXBUILD=sphinx-build-%python3_version
rm -f doc/scapy/_build_doc/html/.buildinfo
rm -f doc/scapy/_build_doc/html/_static/_dummy
%endif
%install
install -dp -m0755 %{buildroot}%{_mandir}/man1
install -Dp -m0644 doc/scapy.1* %{buildroot}%{_mandir}/man1/
%pyproject_install
mv -f %{buildroot}%{_bindir}/scapy   %{buildroot}%{_bindir}/scapy3
ln -s scapy3 %{buildroot}%{_bindir}/scapy
%oreon_autofiles main usr/lib/python3*/site-packages/scapy* usr/lib64/python3*/site-packages/scapy* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%global         check_exclude %{expand:
    -e 'scapy.arch.bpf.core' -e 'scapy.arch.bpf.supersocket' \
    -e 'scapy.arch.windows' -e 'scapy.arch.windows.native' -e 'scapy.arch.windows.structures' \
    -e 'scapy.contrib.cansocket_python_can' -e 'scapy.tools.generate_bluetooth' \
    -e 'scapy.tools.generate_ethertypes' -e 'scapy.tools.generate_manuf' -e 'scapy.tools.scapy_pyannotate' \
    -e 'scapy.libs.winpcapy'
}
%pyproject_check_import %{check_exclude}
%files
%files -n python3-scapy -f %{oreon_filedir}/python3-scapy.list
%files -n scapy-doc -f %{oreon_filedir}/scapy-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.0-1
- Prepare for Oreon 11 (RP1)
