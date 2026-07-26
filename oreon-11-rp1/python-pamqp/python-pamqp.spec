%global source0_hash d205c2599029d2e3c95d3666013899d10300d380eb87580a0e8182003c31f7b3

%global module pamqp
Name:		python-%{module}
Version:	3.3.0
Release:	7%{?dist}
License:	BSD-3-Clause
Summary:	AMQP 0-9-1 library
URL:		https://github.com/gmr/%{module}
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz#/%{module}-%{version}.tar.gz
BuildArch:	noarch

%description
pamqp is a low level AMQP 0-9-1 frame encoding and decoding library for Python3.
pamqp is not a end-user client library for talking to RabbitMQ but rather is
used by client libraries for marshaling and unmarshaling AMQP frames.

%package -n python3-%{module}
Summary:	%{summary}
# python3-devel
BuildRequires:	pkgconfig(python3)
# python3-wheel
BuildRequires:	%{py3_dist wheel}
# python3-pytest
BuildRequires:	%{py3_dist pytest}
%{?python_provide:%python_provide python3-%{module}}

%description -n python3-%{module}
pamqp is a low level AMQP 0-9-1 frame encoding and decoding library for Python3.
pamqp is not a end-user client library for talking to RabbitMQ but rather is
used by client libraries for marshaling and unmarshaling AMQP frames.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{module}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module}

%check
%{pytest}

%files -n python3-%{module} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
