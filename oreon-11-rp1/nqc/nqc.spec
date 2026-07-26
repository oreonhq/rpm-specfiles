%global source0_hash 8e0f4e5523e0a62af222f760a37cd9a74d4a55a70a93c42f256e5528f06cb82b

Name:           nqc
Version:        3.1.7
Release:        41%{?dist}
Summary:        Not Quite C compiler

# Automatically converted from old format: MPLv1.0 - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.0
URL:            http://bricxcc.sourceforge.net/nqc/
Source0:        http://bricxcc.sourceforge.net/nqc/release/nqc-3.1.r6.tgz
Source1:        60-legousbtower.rules
Source2:        http://bricxcc.sourceforge.net/nqc/doc/faq.html
Source3:        http://bricxcc.sourceforge.net/nqc/doc/NQC_Manual.pdf
Source4:        http://bricxcc.sourceforge.net/nqc/doc/NQC_Guide.pdf
Source5:        http://bricxcc.sourceforge.net/nqc/doc/NQC_Tutorial.pdf
Source6:        http://bricxcc.sourceforge.net/nqc/doc/NQCTutorialSamples.zip
Source7:        http://people.cs.uu.nl/markov/lego/tutorial_n.doc
Source8:        http://people.cs.uu.nl/markov/lego/tutorial_d.doc
Source9:        http://people.cs.uu.nl/markov/lego/tutorial_j.pdf
Source10:       http://people.cs.uu.nl/markov/lego/tutorial_s.doc
Source11:       http://people.cs.uu.nl/markov/lego/tutorial_i.doc
Source12:       http://people.cs.uu.nl/markov/lego/tutorial_t.doc
Source13:       http://people.cs.uu.nl/markov/lego/tutorial_p.pdf
Patch0:         nqc-3.1.6-linux.patch
Patch1:         nqc-3.1.6.gcc47.patch
Patch2:         nqc-3.1.6-unistd.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  flex >= 2.5 
BuildRequires:  byacc
BuildRequires:  systemd-rpm-macros

%description
Not Quite C is a simple language with a C-like syntax that can be used to
program Lego's RCX programmable brick (from the Mindstorms set).

%package        doc
Summary:        English Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-en)

%description    doc
English Documentation for NQC

%package        doc-nl
Summary:        Dutch Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-nl)

%description	doc-nl
Dutch Documentation for NQC

%package        doc-de
Summary:        German Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-de)

%description	doc-de
German Documentation for NQC

%package        doc-ja
Summary:        Japanese Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-ja)

%description	doc-ja
Japanese Documentation for NQC

%package        doc-es
Summary:        Spanish Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-es)

%description	doc-es
Spanish Documentation for NQC

%package        doc-it
Summary:        Italian Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-it)

%description	doc-it
Italian Documentation for NQC

%package        doc-th
Summary:        Thai Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-th)

%description	doc-th
Thai Documentation for NQC

%package        doc-pt
Summary:        Portuguese Documentation for NQC
Supplements:    (%{name} = %{version}-%{release} and langpacks-pt)

%description	doc-pt
Portuguese Documentation for NQC

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q -n nqc-3.1.r6
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p0 -b .isatty

for i in %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
  %{__cp} --preserve=timestamps $i .
done

%{__cp} --preserve=timestamps %{SOURCE7} ./nqc-tutorial-nl.doc
%{__cp} --preserve=timestamps %{SOURCE8} ./nqc-tutorial-de.doc
%{__cp} --preserve=timestamps %{SOURCE9} ./nqc-tutorial-ja.pdf
%{__cp} --preserve=timestamps %{SOURCE10} ./nqc-tutorial-es.doc
%{__cp} --preserve=timestamps %{SOURCE11} ./nqc-tutorial-it.doc
%{__cp} --preserve=timestamps %{SOURCE12} ./nqc-tutorial-th.doc
%{__cp} --preserve=timestamps %{SOURCE13} ./nqc-tutorial-pt.pdf

%{__mkdir} tutorial_files
%{__unzip} -qq -a %{SOURCE6} -d tutorial_files

# This piece of software seems to come from the Dark Side. Fix permissions and
# line endings.
find -type f -exec chmod 644 {} \; -exec perl -pi -e 's/\r\n/\n/g' {} \;

# Create a sysusers.d config file
cat >nqc.sysusers.conf <<EOF
g lego -
EOF

%build
%make_build

%install
%make_install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man1
rm %{buildroot}%{_bindir}/mkdata
install -p -m0644 -D %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-legousbtower.rules
install -m0644 -D nqc.sysusers.conf %{buildroot}%{_sysusersdir}/nqc.conf

%files
%{_bindir}/nqc
%{_mandir}/man1/nqc.1.gz
%{_udevrulesdir}/60-legousbtower.rules
%doc readme.txt LICENSE
%{_sysusersdir}/nqc.conf

%files doc
%doc scout.txt history.txt test.nqc
%doc faq.html NQC_Manual.pdf NQC_Guide.pdf NQC_Tutorial.pdf tutorial_files/

%files doc-nl
%lang(nl) %doc nqc-tutorial-nl.doc

%files doc-de
%lang(de) %doc nqc-tutorial-de.doc

%files doc-ja
%lang(ja) %doc nqc-tutorial-ja.pdf

%files doc-es
%lang(es) %doc nqc-tutorial-es.doc

%files doc-it
%lang(it) %doc nqc-tutorial-it.doc

%files doc-th
%lang(th) %doc nqc-tutorial-th.doc

%files doc-pt
%lang(pt) %doc nqc-tutorial-pt.pdf

%changelog
%autochangelog
