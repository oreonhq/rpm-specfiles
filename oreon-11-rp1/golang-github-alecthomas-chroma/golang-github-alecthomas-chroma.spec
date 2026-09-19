%global source0_hash 1294c3afca183dead839fd283f08068dbbb94170cd8a217400f4bd92dbcfe053

# https://github.com/alecthomas/chroma
%global goipath         github.com/alecthomas/chroma
Version:                2.15.0

%gometa

%global common_description %{expand:
Chroma takes source code and other structured text and converts it into syntax
highlighted HTML, ANSI-coloured text, etc.

Chroma is based heavily on Pygments, and includes translators for Pygments
lexers and styles.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        General purpose syntax highlighter in pure Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license COPYING
%doc README.md
%{_bindir}/chroma
%{_bindir}/chromad

%gopkgfiles

%changelog
%autochangelog
