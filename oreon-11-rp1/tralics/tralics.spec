%global source0_hash 701ba90cb0a09a2b42527d9ecf1b9809e277703ba1d8158bfc4c1d9072826700

Name:           tralics
Version:        2.15.4
Release:        %autorelease
Summary:        LaTeX to XML translator
# Automatically converted from old format: CeCILL - review is highly recommended.
License:        CECILL-2.1
URL:            https://www-sop.inria.fr/marelle/tralics/
Source0:        ftp://ftp-sop.inria.fr/marelle/tralics/src/%{name}-src-%{version}.tar.gz

Patch0:         testkeyval.diff

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  texlive-collection-latexextra

%description
Tralics is a free software whose purpose is to convert a LaTeX document into 
an XML file. It is used since 2002 for instance to produce the INRIA's 
annual activity report.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for f in Licence_CeCILL_V2-en.txt ChangeLog
    do
      iconv -f ISO-8859-15 -t utf-8	\
      ${f} > ${f}.conv &&               \
      touch -r ${f} ${f}.conv &&        \
      mv -f ${f}.conv ${f}
    done
sed -i 's|tralics $(OBJECTS)|tralics $(OBJECTS) $(LDFLAGS)|' src/Makefile

%build
%make_build -C src/ CPPFLAGS="%{optflags}                     \
                    -DTRALICSDIR=\\\"%{_datadir}/%{name}\\\"  \
                    -DCONFDIR=\\\"%{_sysconfdir}/%{name}\\\"" \
                    LDFLAGS="%{?__global_ldflags}"

%install
rm -frv confdir/{README,COPYING}
install -pDm755 src/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm644 confdir/* %{buildroot}%{_datadir}/%{name}/

%check
cd Test && ./alltests

%files
%doc ChangeLog README
%license COPYING Copyright Licence_CeCILL_V2-en.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
%autochangelog
