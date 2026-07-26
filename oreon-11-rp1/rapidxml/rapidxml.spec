%global source0_hash 198aa69876a3f3f47937776df3c750417dae4e778c44655dc66b778f00e59bcf

Name:           rapidxml
Version:        1.13
Release:        28%{?dist}
Summary:        Fast XML parser
License:        BSL-1.0 OR MIT
URL:            http://rapidxml.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-with-tests.zip
Patch0:         %{name}-declarations.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  dos2unix

%description
RapidXml is an attempt to create the fastest XML parser possible, while
retaining usability, portability and reasonable W3C compatibility. It is an
in-situ parser written in modern C++, with parsing speed approaching that of
strlen function executed on the same data.

%package devel
Summary:       Fast XML parser
Provides:      %{name}-static = %{version}-%{release}

%description devel
RapidXml is an attempt to create the fastest XML parser possible, while
retaining usability, portability and reasonable W3C compatibility. It is an
in-situ parser written in modern C++, with parsing speed approaching that of
strlen function executed on the same data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}-with-tests
%patch -P0 -p1

dos2unix license.txt

# Rename it to .h (but keep .hpp for tests)
sed -i 's/.hpp/.h/g' manual.html
for HPP in *.hpp; do
  cp -p $HPP ${HPP%hpp}h
  sed -i 's/.hpp/.h/g' ${HPP%hpp}h
done

%build
cd tests
# -jX is useless here
make build-g++-debug
cd -

%install
for H in *.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%check
cd tests
# -jX is useless here
make run-g++-debug
cd -

%files devel
%doc license.txt manual.html
%{_includedir}/*

%changelog
%autochangelog
