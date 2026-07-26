%global source0_hash 0ba244eb65a4c9db180b3223458acc9cce425ae5931ae4ccaad5a2cb351094aa

Name:           python-precis_i18n
Version:        1.1.2
Release:        2%{?dist}
Summary:        Python library for internationalized usernames and passwords

License:        MIT
URL:            https://github.com/byllyfish/precis_i18n
Source0:        https://github.com/byllyfish/precis_i18n/archive/v%{version}.tar.gz#/precis_i18n-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global desc %{expand:
If you want your application to accept Unicode user names and passwords, you
must be careful in how you validate and compare them. The PRECIS framework
makes internationalized user names and passwords safer for use by applications.
PRECIS profiles transform Unicode strings into a canonical form, suitable for
comparison.

This Python module implements the PRECIS Framework as described in:

  PRECIS Framework: Preparation, Enforcement, and Comparison of
  Internationalized Strings in Application Protocols (RFC 8264)

  Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Usernames and Passwords (RFC 8265)

  Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Nicknames (RFC 8266)}

%description
%{desc}

%package -n python3-precis_i18n
Summary:        %{summary}

%description -n python3-precis_i18n
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n precis_i18n-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l precis_i18n

%check
%pytest

%files -n python3-precis_i18n -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
