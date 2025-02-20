import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Mail:
	html_template = """
	<body style="background-color: #000000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f1f1f1;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #9966ff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 600px;" width="600">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; border-bottom: 0px dotted transparent; border-left: 0px dotted transparent; border-right: 0px dotted transparent; border-top: 0px dotted transparent; vertical-align: top; padding-top: 32px; padding-bottom: 32px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img src="https://www.gov.br/ibama/pt-br/phocadownload/manuais/teste.png" style="display: block; height: auto; border: 0; width: 250px; max-width: 100%;" width="250"></div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 15px 0">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0 10px; color: #000000; width: 600px; background-color: #ffffff;" width="600">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 32px; padding-right: 32px; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:16px;padding-top:16px;text-align:center;width:100%;">
																<h1 style="margin: 0; color: #131313; direction: ltr; font-family:'Barlow', sans-serif; font-size: 24px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 10px;"><span class="tinyMce-placeholder">Solicitação de Transferência nº{id_solicitacao}: Códigos de Cliente Não Identificados ou Duplicados
                                                                </span></h1>
																<hr>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#242424;direction:ltr;font-family:'Barlow', sans-serif;font-size:14px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:left;mso-line-height-alt:18px;">
																	<p style="margin: 0;">	Olá, tudo bem? 
                                                                        <br><br>
																		O sistema identificou que alguns dos códigos de cliente solicitados para transferência foram rejeitados pelo sistema.
																		<br><br>
																		Seguem os códigos abaixo:
																		{corpo_email}
																		<br><br>
																		Em caso necessário, favor entrar em contato com a Iris.

                                                                        
																						<table class="paragraph_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
																							<tr>
																								<td class="pad">
																									<table class="button_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																										<tr>
																											<td class="pad" style="padding-bottom:40px;padding-top:12px;text-align:left;">
																												<div class="alignment" align="center">
																													<!--[if mso]><![endif]-->
																													<div style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#9966ff;border-radius:2px;width:auto;font-weight:500;padding-top:5px;padding-bottom:5px;font-family:'Barlow', sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:15px;padding-right:15px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;"><a href="https://api.whatsapp.com/send/?phone=&text&type=phone_number&app_absent=0" style="text-decoration:none; color: #ffffff;">Contato</a></span></span></div>
																													<!--[if mso]><![endif]-->
																													
																												</div>
																											</td>
																										</tr>
																							</tr>
																						</table>
                                                                                        Atenciosamente,<br>
                                                                                        <i>área de atendimento</i>.
																						<br><br><br>                                                                                                                                                
                                                                    </p>
																</div>
															</td>
														</tr>
													</table>
															</td>
														</tr>
													</table>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>

					<table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #ffffff; width: 600px;" width="600">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="social_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding:10px;text-align:center;">
																<div class="alignment" style="text-align:center;">
																	<table class="social-table" width="96px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
																		<tr>
																			<td style="padding:0 2px 0 2px;"><a href="" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/instagram@2x.png" style="display: block; height: 28px; border: 0;"></a></td>
																			<td style="padding:0 2px 0 2px;"><a href="" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/linkedin@2x.png" style="display: block; height: 28px; border: 0;"></a></td>
                                                                            <td style="padding:0 2px 0 2px;"><a href="" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/facebook@2x.png" style="display: block; height: 28px; border: 0;"></a></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
                                                    
                                                    <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding:10px 0 5px 0;width:100%;">
																<div class="alignment" align="center" style="line-height:10px; margin-bottom: 20px;"><img src="https://static3.tcdn.com.br/img/img_prod/460977/teste_100485_1_cbc226c7d23a19c784fb4752ffe61337.png" style="display: block; height: auto; border: 0; width: 200px; max-width: 100%;" width="200"></div>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#F8F1ED;direction:ltr;font-family:'Barlow', sans-serif;font-size:14px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:center;mso-line-height-alt:16.8px;">
																	<p style="margin: 0 0 10px 0;">Copyright © ****** - Todos os direitos reservados</p>
																</div>
															</td>
														</tr>
													</table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </body>
		"""

	def __init__(
        self, smtp_server=None, smtp_port=None, smtp_username=None, smtp_password=None
    ):
		self.smtp_server = smtp_server
		self.smtp_port = smtp_port
		self.smtp_username = smtp_username
		self.smtp_password = smtp_password

	def connection(self):
		server = smtplib.SMTP(self.smtp_server, self.smtp_port)
		server.starttls()
		server.login(self.smtp_username, self.smtp_password)
		return server
	
	def send(self, subject, email, cc=None, caminho=None, filename=None, corpo_email=None, id_solicitacao=None):
		try:
			html = self.html_template.format(corpo_email=corpo_email, id_solicitacao=id_solicitacao)
			message = MIMEMultipart()
			if caminho is not None:
				with open(caminho, "rb") as file:
					attachment = MIMEApplication(file.read(), _subtype="xlsx")
					attachment.add_header("Content-Disposition", "attachment", filename=filename)
					message.attach(attachment)
			message["Subject"] = subject
			message["From"] = self.smtp_username
			message["To"] = email
			if cc:
				message["Cc"] = cc
			message.attach(MIMEText(html, "html"))

			server = self.connection()
			server.send_message(message)
			server.quit()
			print("Email enviado com sucesso!")
		except Exception as e:
			print(f"Erro ao enviar o e-mail: {e}")


# email_login = "hub@investsmart.com.br"
# dw_pass_login = "Bitrix!admin"
# conexao = Mail(
#     "smtp.office365.com",
#     587,
#     email_login,
#     dw_pass_login,
# )


# corpo_email = "oioioi"
# id_solicitacao = "121231"

# conexao.send(
#     subject=f"Teste",
# 	id_solicitacao=id_solicitacao,
# 	corpo_email=corpo_email,
#     email="matheus.santana@investsmart.com.br"
#     )