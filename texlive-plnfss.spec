%global tl_name plnfss
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Font selection for Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/plnfss
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plnfss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plnfss.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Plnfss is a set of macros to provide easy font access (somewhat similar
to NFSS but with some limitations) with Plain TeX. Plnfss can
automatically make use of PSNFSS fd files, i.e., when an Adobe Type 1 is
used the relevant fd file will be loaded automatically. For cmr-like
fonts (ec, vnr, csr or plr fonts), a special format called pfd (plain
fd) is required and must be loaded manually. See ot1cmr.pfd for further
information.

